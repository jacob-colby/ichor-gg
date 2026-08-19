---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.39
  aspect_win_rate: 0.54
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.28
    win_rate: 0.48
    alternates:
    - name: Tyrfing
      pick_rate: 0.21
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.56
  - name: The World Stone
    pick_rate: 0.15
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.49
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.59
  - name: Soul Gem
    pick_rate: 0.1
    win_rate: 0.51
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.56
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.48
  - name: Rod of Tahuti
    pick_rate: 0.19
    win_rate: 0.57
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.49
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.6
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.47
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.45
    - name: Silverbranch Bow
      pick_rate: 0.06
      win_rate: 0.53
  - name: Hunter's Bow
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.57
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.31
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.17
    win_rate: 0.54
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.45
  - name: Death's Embrace
    pick_rate: 0.14
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-08-19'
  god_win_rate: 0.5150501672240803
  god_matches_won: 308
  god_matches_played: 598
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Death
    Metal, Berserker''s Shield, Genji''s Guard, Riptalon, Damaru, The Cosmic Horror,
    Spear of the Magus, Hydra''s Lament, Lernaean Bow, Golden Blade, The Reaper, Breastplate
    of Valor, Bragi''s Harp, Bracer of The Abyss, Dominance, Chronos'' Pendant, Runeforged
    Hammer, Tekko-Kagi, Blood-Bound Book, Pharaoh''s Curse, Kinetic Cuirass, Bancroft''s
    Talon, Amanita Charm, Freya''s Tears, Helm of Radiance, Totem of Death, Ethereal
    Staff, Heartseeker, Eye of Providence, Rod of Asclepius, Oni Hunter''s Garb, Titan''s
    Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.35
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.3
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Nimble
    Ring, Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Death Metal, Genji''s
    Guard, Hydra''s Lament, Berserker''s Shield, Damaru, The Cosmic Horror, Breastplate
    of Valor, Spear of the Magus, Lernaean Bow, Dominance, Bragi''s Harp, Riptalon,
    Golden Blade, The Reaper, Runeforged Hammer, Bancroft''s Talon, Chronos'' Pendant,
    Bracer of The Abyss, Blood-Bound Book, Heartseeker, Oni Hunter''s Garb, Tekko-Kagi,
    Kinetic Cuirass, Helm of Radiance, Totem of Death, Amanita Charm, Ethereal Staff,
    Freya''s Tears, Transcendence, Rod of Asclepius, Pharaoh''s Curse, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Death Metal
  - Gluttonous Grimoire
  - Damaru
  - The Crusher
  - Deathbringer
  - Rod of Tahuti
  flex_slots:
  - Damaru
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Death
    Metal, Berserker''s Shield, Genji''s Guard, Damaru, The Cosmic Horror, Riptalon,
    Spear of the Magus, Hydra''s Lament, Lernaean Bow, Breastplate of Valor, The Reaper,
    Golden Blade, Bragi''s Harp, Bracer of The Abyss, Dominance, Chronos'' Pendant,
    Runeforged Hammer, Blood-Bound Book, Tekko-Kagi, Kinetic Cuirass, Bancroft''s
    Talon, Amanita Charm, Pharaoh''s Curse, Freya''s Tears, Helm of Radiance, Ethereal
    Staff, Totem of Death, Eye of Providence, Heartseeker, Oni Hunter''s Garb, Rod
    of Asclepius, Titan''s Bane.'
  slot_scores:
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.48
    Damaru:
      total: 0.49
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.37
    Deathbringer:
      total: 0.45
      efficiency: 0.45
      win: 0.53
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Nimble Ring, Jotunn''s Revenge, The Crusher, Genji''s
    Guard, Death Metal, Berserker''s Shield, The Cosmic Horror, Riptalon, Hydra''s
    Lament, Spear of the Magus, Damaru, Breastplate of Valor, The Reaper, Lernaean
    Bow, Golden Blade, Chronos'' Pendant, Tekko-Kagi, Runeforged Hammer, Bragi''s
    Harp, Dominance, Freya''s Tears, Bracer of The Abyss, Heartseeker, Kinetic Cuirass,
    Blood-Bound Book, Totem of Death, Titan''s Bane, Amanita Charm, Shield of the
    Phoenix, Pharaoh''s Curse, Eye of Providence, Bancroft''s Talon, Oni Hunter''s
    Garb, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.46
    Transcendence:
      total: 0.44
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.13
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.37
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - The Crusher
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Gluttonous Grimoire, Nimble Ring, Shield of the Phoenix,
    Berserker''s Shield, Riptalon, Ethereal Staff, Rod of Asclepius, The Crusher,
    Kinetic Cuirass, The Reaper, Genji''s Guard, Blood-Bound Book, Jotunn''s Revenge,
    Yogi''s Necklace, Chandra''s Grace, Bancroft''s Talon, Death Metal, Breastplate
    of Valor, Oni Hunter''s Garb, Pharaoh''s Curse, Freya''s Tears, Runeforged Hammer,
    Golden Blade, Lifebinder, The Cosmic Horror, Phoenix Feather, Damaru, Hydra''s
    Lament, Spectral Armor, Spear of the Magus, Shogun''s Ofuda, Lernaean Bow, Erosion,
    Shifter''s Shield, Helm of Radiance, Umbral Link, Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.3
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.21
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.51
      pick: 0.16
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Cosmic Horror
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Nimble Ring, Jotunn''s Revenge,
    The Cosmic Horror, Riptalon, Spear of the Magus, Death Metal, Berserker''s Shield,
    Genji''s Guard, The Reaper, Avenging Blade, Screeching Gargoyle, Damaru, Tekko-Kagi,
    Hydra''s Lament, Lernaean Bow, Breastplate of Valor, Heartseeker, Golden Blade,
    Titan''s Bane, Stone of Binding, Bracer of The Abyss, Runeforged Hammer, Bragi''s
    Harp, Dominance, Doom Orb, Kinetic Cuirass, Chronos'' Pendant, Blood-Bound Book,
    Void Shield, Amanita Charm, Pharaoh''s Curse, Toxic Blade, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.57
    The Cosmic Horror:
      total: 0.5
      efficiency: 0.58
      win: 0.53
      pick: 0.0
      fit: 0.4
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Riptalon
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Riptalon,
    Berserker''s Shield, Death Metal, Genji''s Guard, Golden Blade, The Cosmic Horror,
    Damaru, Spear of the Magus, Hydra''s Lament, Lernaean Bow, Breastplate of Valor,
    Bracer of The Abyss, The Reaper, Bragi''s Harp, Dominance, Runeforged Hammer,
    Kinetic Cuirass, Pharaoh''s Curse, Chronos'' Pendant, Blood-Bound Book, Amanita
    Charm, Toxic Blade, Tekko-Kagi, Eye of Providence, Freya''s Tears, Bancroft''s
    Talon, Oni Hunter''s Garb, Helm of Radiance, Ethereal Staff, Totem of Death, Rod
    of Asclepius, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.3
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.5
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.46
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Genji''s
    Guard, Gluttonous Grimoire, The Crusher, Breastplate of Valor, Hydra''s Lament,
    Berserker''s Shield, Death Metal, Freya''s Tears, Chronos'' Pendant, Riptalon,
    Shield of the Phoenix, Damaru, The Cosmic Horror, Totem of Death, Spear of the
    Magus, Lernaean Bow, Screeching Gargoyle, Chandra''s Grace, Golden Blade, Gem
    of Focus, The Reaper, Kinetic Cuirass, Amanita Charm, Runeforged Hammer, Arondight,
    Dominance, Pharaoh''s Curse, Bracer of The Abyss, Pendulum Blade, Eye of Providence,
    Oni Hunter''s Garb, Blood-Bound Book, Tekko-Kagi, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.53
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.31
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.31
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.51
      pick: 0.16
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Gluttonous Grimoire, Jotunn''s
    Revenge, The Crusher, Death Metal, Genji''s Guard, Berserker''s Shield, The Cosmic
    Horror, Spear of the Magus, Riptalon, Hydra''s Lament, Damaru, Breastplate of
    Valor, Chronos'' Pendant, Bracer of The Abyss, Bragi''s Harp, Lernaean Bow, Blood-Bound
    Book, The Reaper, Golden Blade, Totem of Death, Bancroft''s Talon, Helm of Radiance,
    Runeforged Hammer, Ethereal Staff, Dominance, Rod of Asclepius, Kinetic Cuirass,
    Freya''s Tears, Amanita Charm, Tekko-Kagi, Pharaoh''s Curse, Gem of Focus, Jade
    Scepter, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.32
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Nimble Ring, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Death Metal, Berserker''s Shield, Genji''s Guard,
    Damaru, The Cosmic Horror, Hydra''s Lament, Spear of the Magus, Riptalon, Lernaean
    Bow, Bragi''s Harp, The Reaper, Golden Blade, Breastplate of Valor, Dominance,
    Runeforged Hammer, Bracer of The Abyss, Tekko-Kagi, Chronos'' Pendant, Blood-Bound
    Book, Kinetic Cuirass, Bancroft''s Talon, Heartseeker, Amanita Charm, Helm of
    Radiance, Pharaoh''s Curse, Ethereal Staff, Totem of Death, Titan''s Bane, Rod
    of Asclepius, Freya''s Tears, Eye of Providence, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.53
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.6
      pick: 0.17
      fit: 0.33
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.41
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Nimble Ring, Gluttonous Grimoire, The Crusher, Jotunn''s
    Revenge, Death Metal, Berserker''s Shield, Genji''s Guard, Riptalon, Damaru, The
    Cosmic Horror, Spear of the Magus, Hydra''s Lament, Lernaean Bow, Golden Blade,
    The Reaper, Breastplate of Valor, Bragi''s Harp, Bracer of The Abyss, Dominance,
    Chronos'' Pendant, Runeforged Hammer, Tekko-Kagi, Blood-Bound Book, Pharaoh''s
    Curse, Kinetic Cuirass, Bancroft''s Talon, Amanita Charm, Freya''s Tears, Helm
    of Radiance, Totem of Death, Ethereal Staff, Heartseeker, Eye of Providence, Rod
    of Asclepius, Oni Hunter''s Garb, Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.57
      pick: 0.32
      fit: 0.3
  starter: *id001
---
