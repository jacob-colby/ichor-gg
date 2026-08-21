---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.38
  aspect_win_rate: 0.55
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.27
    win_rate: 0.5
    alternates:
    - name: Tyrfing
      pick_rate: 0.21
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.55
  - name: The World Stone
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.13
      win_rate: 0.53
    - name: Odysseus' Bow
      pick_rate: 0.11
      win_rate: 0.62
  - name: Rod of Tahuti
    pick_rate: 0.11
    win_rate: 0.58
    alternates:
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.49
    - name: The World Stone
      pick_rate: 0.09
      win_rate: 0.49
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.56
    - name: Silverbranch Bow
      pick_rate: 0.1
      win_rate: 0.62
  - name: The Executioner
    pick_rate: 0.07
    win_rate: 0.7
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.12
      win_rate: 0.46
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.44
  - name: Hunter's Bow
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Evil Eye
      pick_rate: 0.06
      win_rate: 0.31
    - name: Manchu Bow
      pick_rate: 0.06
      win_rate: 0.62
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.18
    win_rate: 0.53
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.49
  - name: Death's Embrace
    pick_rate: 0.13
    win_rate: 0.58
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-08-21'
  god_win_rate: 0.5279583875162549
  god_matches_won: 406
  god_matches_played: 769
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Gluttonous Grimoire, Berserker''s
    Shield, Soul Gem, The Crusher, Spear of the Magus, Riptalon, Lernaean Bow, The
    Reaper, Genji''s Guard, Breastplate of Valor, Bragi''s Harp, Tekko-Kagi, Golden
    Blade, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Runeforged Hammer, Helm
    of Radiance, Amanita Charm, Doom Orb, The Cosmic Horror, Freya''s Tears, Kinetic
    Cuirass, Chronos'' Pendant, Deathbringer, Damaru, Ancient Signet, Ethereal Staff,
    Pharaoh''s Curse, Blood-Bound Book, Rod of Asclepius, Dreamer''s Idol, Titan''s
    Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.17
      fit: 0.39
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.29
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Death Metal, Nimble Ring, Gluttonous Grimoire, Berserker''s Shield, Soul
    Gem, The Crusher, Spear of the Magus, Hydra''s Lament, Genji''s Guard, Breastplate
    of Valor, Bragi''s Harp, Lernaean Bow, Heartseeker, The Reaper, Runeforged Hammer,
    Golden Blade, Tekko-Kagi, Ancient Signet, Doom Orb, Helm of Radiance, Riptalon,
    Bracer of The Abyss, Chronos'' Pendant, Amanita Charm, Dominance, Freya''s Tears,
    Kinetic Cuirass, The Cosmic Horror, Deathbringer, Damaru, Ethereal Staff, Rod
    of Asclepius, Bancroft''s Talon, Wish-Granting Pearl, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.42
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.54
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.44
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.62
      pick: 0.17
      fit: 0.31
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - Damaru
  - Deathbringer
  - Rod of Tahuti
  flex_slots:
  - Deathbringer
  - Damaru
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
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Gluttonous Grimoire, Berserker''s
    Shield, Soul Gem, Spear of the Magus, The Crusher, Riptalon, Genji''s Guard, The
    Reaper, Breastplate of Valor, Lernaean Bow, Bragi''s Harp, Tekko-Kagi, Hydra''s
    Lament, Golden Blade, Heartseeker, Bracer of The Abyss, Runeforged Hammer, Helm
    of Radiance, Amanita Charm, Deathbringer, Damaru, Doom Orb, The Cosmic Horror,
    Freya''s Tears, Kinetic Cuirass, Chronos'' Pendant, Ancient Signet, Ethereal Staff,
    Rod of Asclepius, Blood-Bound Book, Dreamer''s Idol, Pharaoh''s Curse, Titan''s
    Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.33
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.17
      fit: 0.37
    Damaru:
      total: 0.47
      efficiency: 0.5
      win: 0.54
      pick: 0.0
      fit: 0.34
    Deathbringer:
      total: 0.47
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.34
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    god: Jotunn''s Revenge, Gluttonous Grimoire, Nimble Ring, Death Metal, Soul Gem,
    Berserker''s Shield, The Crusher, Spear of the Magus, Genji''s Guard, The Reaper,
    Breastplate of Valor, Riptalon, Hydra''s Lament, Tekko-Kagi, Heartseeker, Lernaean
    Bow, Freya''s Tears, Bragi''s Harp, Doom Orb, Golden Blade, The Cosmic Horror,
    Runeforged Hammer, Chronos'' Pendant, Amanita Charm, Titan''s Bane, Helm of Radiance,
    Kinetic Cuirass, Bracer of The Abyss, Dreamer''s Idol, Toxic Blade, Deathbringer,
    Ancient Signet, Damaru, Ethereal Staff, Shield of the Phoenix, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.13
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.13
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.17
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Shield
    of the Phoenix, Gluttonous Grimoire, Ethereal Staff, Rod of Asclepius, The Reaper,
    Riptalon, Nimble Ring, Kinetic Cuirass, Death Metal, Blood-Bound Book, Genji''s
    Guard, Breastplate of Valor, Freya''s Tears, Bancroft''s Talon, The Crusher, Pharaoh''s
    Curse, Yogi''s Necklace, Spear of the Magus, Runeforged Hammer, Chandra''s Grace,
    Phoenix Feather, Golden Blade, Lifebinder, Helm of Radiance, Shogun''s Ofuda,
    Shifter''s Shield, Sphere of Negation, Mantle Of Discord, Shield Splitter, Stone
    of Binding, Lernaean Bow, Spectral Armor, Hydra''s Lament.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.11
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.25
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.21
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.58
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.49
      pick: 0.14
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - The Executioner
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Gluttonous Grimoire, Nimble Ring, Soul Gem, Death
    Metal, The Crusher, Spear of the Magus, Berserker''s Shield, Riptalon, The Reaper,
    Tekko-Kagi, Stone of Binding, Avenging Blade, Screeching Gargoyle, Heartseeker,
    Doom Orb, The Cosmic Horror, Genji''s Guard, Breastplate of Valor, Lernaean Bow,
    Titan''s Bane, Dreamer''s Idol, Toxic Blade, Hydra''s Lament, Bragi''s Harp, Golden
    Blade, Amanita Charm, Runeforged Hammer, Helm of Radiance, Bracer of The Abyss,
    Kinetic Cuirass, Freya''s Tears, Void Shield, Chronos'' Pendant, Ancient Signet,
    Void Stone.'
  slot_scores:
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.7
      pick: 0.15
      fit: 0.57
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.43
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.62
      pick: 0.17
      fit: 0.47
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Book of Thoth
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
    this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Gluttonous Grimoire, Berserker''s
    Shield, Soul Gem, Riptalon, The Crusher, Spear of the Magus, Golden Blade, Lernaean
    Bow, Genji''s Guard, Breastplate of Valor, The Reaper, Bragi''s Harp, Tekko-Kagi,
    Bracer of The Abyss, Hydra''s Lament, Toxic Blade, Amanita Charm, Runeforged Hammer,
    Heartseeker, Helm of Radiance, Kinetic Cuirass, Freya''s Tears, Doom Orb, The
    Cosmic Horror, Pharaoh''s Curse, Chronos'' Pendant, Ancient Signet, Ethereal Staff,
    Deathbringer, Damaru, Rod of Asclepius, Dominance, Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.13
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.3
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.62
      pick: 0.17
      fit: 0.46
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Berserker''s
    Shield, Death Metal, Hydra''s Lament, Freya''s Tears, The Crusher, Chronos'' Pendant,
    Spear of the Magus, Riptalon, Shield of the Phoenix, Lernaean Bow, Screeching
    Gargoyle, The Reaper, Amanita Charm, Arondight, Tekko-Kagi, Gem of Focus, Golden
    Blade, Kinetic Cuirass, Runeforged Hammer, Heartseeker, Helm of Radiance, Bragi''s
    Harp, Bracer of The Abyss, Totem of Death, Pharaoh''s Curse, Pendulum Blade, Doom
    Orb, Eye of Providence, The Cosmic Horror, Deathbringer, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.08
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.54
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.47
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.08
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.49
      pick: 0.14
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
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
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal,
    Gluttonous Grimoire, Soul Gem, Berserker''s Shield, Spear of the Magus, The Crusher,
    Genji''s Guard, Breastplate of Valor, Bragi''s Harp, Riptalon, Helm of Radiance,
    Bracer of The Abyss, Lernaean Bow, The Reaper, Chronos'' Pendant, Hydra''s Lament,
    Doom Orb, The Cosmic Horror, Tekko-Kagi, Ancient Signet, Golden Blade, Freya''s
    Tears, Ethereal Staff, Heartseeker, Amanita Charm, Runeforged Hammer, Rod of Asclepius,
    Blood-Bound Book, Dreamer''s Idol, Kinetic Cuirass, Gem of Focus, Jade Scepter,
    Deathbringer, Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.35
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.11
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Death Metal, Nimble
    Ring, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, The Crusher, Spear of
    the Magus, Lernaean Bow, The Reaper, Bragi''s Harp, Riptalon, Tekko-Kagi, Genji''s
    Guard, Hydra''s Lament, Golden Blade, Breastplate of Valor, Heartseeker, Runeforged
    Hammer, Bracer of The Abyss, Helm of Radiance, Doom Orb, The Cosmic Horror, Amanita
    Charm, Deathbringer, Damaru, Chronos'' Pendant, Kinetic Cuirass, Ancient Signet,
    Freya''s Tears, Titan''s Bane, Ethereal Staff, Rod of Asclepius, Dominance, Blood-Bound
    Book, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.18
      fit: 0.16
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.37
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.16
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Gluttonous Grimoire, Berserker''s Shield, The Crusher, Spear of the Magus, Riptalon,
    Lernaean Bow, The Reaper, Genji''s Guard, Breastplate of Valor, Bragi''s Harp,
    Tekko-Kagi, Golden Blade, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Runeforged
    Hammer, Helm of Radiance, Amanita Charm, Doom Orb, The Cosmic Horror, Freya''s
    Tears, Kinetic Cuirass, Chronos'' Pendant, Deathbringer, Damaru, Ancient Signet,
    Ethereal Staff, Pharaoh''s Curse, Blood-Bound Book, Rod of Asclepius, Dreamer''s
    Idol, Titan''s Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.34
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.29
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.14
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - The Executioner
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - The Executioner
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death
    Metal, Soul Gem, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Spear
    of the Magus, Riptalon, Lernaean Bow, The Reaper, Genji''s Guard, Breastplate
    of Valor, Bragi''s Harp, Tekko-Kagi, Golden Blade, Hydra''s Lament, Bracer of
    The Abyss, Heartseeker, Runeforged Hammer, Helm of Radiance, Amanita Charm, Doom
    Orb, The Cosmic Horror, Freya''s Tears, Kinetic Cuirass, Chronos'' Pendant, Deathbringer,
    Damaru, Ancient Signet, Ethereal Staff, Pharaoh''s Curse, Blood-Bound Book, Rod
    of Asclepius, Dreamer''s Idol, Titan''s Bane.'
  slot_scores:
    The Executioner:
      total: 0.49
      efficiency: 0.35
      win: 0.7
      pick: 0.15
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.34
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.58
      pick: 0.17
      fit: 0.29
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.14
      fit: 0.54
  swaps:
  - added: The Executioner
    removed: Berserker's Shield
    reason: community 70% win over 54 matches (vs 53% on this god), taking the model's
      weakest slot from Berserker's Shield
  starter: *id001
---
