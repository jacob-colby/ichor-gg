---
type: smite-build
god: Cernunnos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Strife
  aspect_pick_rate: 0.4
  aspect_win_rate: 0.58
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.41
    win_rate: 0.63
    alternates:
    - name: Tyrfing
      pick_rate: 0.27
      win_rate: 0.45
    - name: Daybreak Gavel
      pick_rate: 0.03
      win_rate: 0.44
  - name: Dagger of Frenzy
    pick_rate: 0.29
    win_rate: 0.65
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.56
    - name: Toxic Blade
      pick_rate: 0.1
      win_rate: 0.56
  - name: Odysseus' Bow
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Riptalon
      pick_rate: 0.15
      win_rate: 0.63
    - name: Dagger of Frenzy
      pick_rate: 0.11
      win_rate: 0.62
  - name: Riptalon
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.12
      win_rate: 0.63
    - name: Dominance
      pick_rate: 0.1
      win_rate: 0.62
  - name: Silverbranch Bow
    pick_rate: 0.12
    win_rate: 0.79
    alternates:
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.62
    - name: Hunter's Bow
      pick_rate: 0.07
      win_rate: 0.5
  - name: Manchu Bow
    pick_rate: 0.1
    win_rate: 0.59
    alternates:
    - name: Bow
      pick_rate: 0.07
      win_rate: 0.33
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.78
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.38
    win_rate: 0.69
  - name: Leather Cowl
    pick_rate: 0.2
    win_rate: 0.4
  - name: Sharpshooter's Arrow
    pick_rate: 0.14
    win_rate: 0.72
  source_url: https://smitebrain.com/gods/cernunnos/
  last_verified: '2026-08-16'
  god_win_rate: 0.5757575757575758
  god_matches_won: 152
  god_matches_played: 264
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-16'
  god_matches_analyzed: 6103
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
    this god: Rod of Tahuti, Nimble Ring, Gluttonous Grimoire, The Crusher, Soul Gem,
    Jotunn''s Revenge, Death Metal, Berserker''s Shield, Genji''s Guard, Damaru, The
    Cosmic Horror, Hydra''s Lament, Lernaean Bow, Spear of the Magus, Spear of Desolation,
    Golden Blade, The Reaper, Bragi''s Harp, Breastplate of Valor, Runeforged Hammer,
    Bracer of The Abyss, Tekko-Kagi, Chronos'' Pendant, Obsidian Shard, Blood-Bound
    Book, Kinetic Cuirass, Pharaoh''s Curse, Amanita Charm, Bancroft''s Talon, Freya''s
    Tears, Helm of Radiance, Eye of Providence, Oni Hunter''s Garb, Rod of Asclepius,
    Shield of the Phoenix, Deathbringer, Shogun''s Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.42
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.34
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.29
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - The Crusher
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Nimble Ring, Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Soul
    Gem, Death Metal, Genji''s Guard, Hydra''s Lament, Berserker''s Shield, Damaru,
    The Cosmic Horror, Breastplate of Valor, Spear of the Magus, Lernaean Bow, Spear
    of Desolation, Bragi''s Harp, Golden Blade, The Reaper, Runeforged Hammer, Bancroft''s
    Talon, Chronos'' Pendant, Bracer of The Abyss, Blood-Bound Book, Obsidian Shard,
    Oni Hunter''s Garb, Tekko-Kagi, Kinetic Cuirass, Helm of Radiance, Amanita Charm,
    Freya''s Tears, Transcendence, Rod of Asclepius, Pharaoh''s Curse, Eye of Providence,
    Doom Orb, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.45
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.28
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - The Crusher
  - Deathbringer
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
    this god: Rod of Tahuti, Nimble Ring, Gluttonous Grimoire, Soul Gem, The Crusher,
    Jotunn''s Revenge, Death Metal, Berserker''s Shield, Genji''s Guard, Damaru, The
    Cosmic Horror, Spear of the Magus, Hydra''s Lament, Spear of Desolation, Lernaean
    Bow, Breastplate of Valor, The Reaper, Golden Blade, Bragi''s Harp, Bracer of
    The Abyss, Runeforged Hammer, Chronos'' Pendant, Obsidian Shard, Blood-Bound Book,
    Tekko-Kagi, Kinetic Cuirass, Amanita Charm, Pharaoh''s Curse, Bancroft''s Talon,
    Freya''s Tears, Helm of Radiance, Eye of Providence, Oni Hunter''s Garb, Rod of
    Asclepius, Shield of the Phoenix, Deathbringer, Jade Scepter.'
  slot_scores:
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.41
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.33
    Damaru:
      total: 0.52
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.37
    Deathbringer:
      total: 0.48
      efficiency: 0.45
      win: 0.6
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Death Metal
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, Soul Gem, Jotunn''s Revenge,
    The Crusher, Genji''s Guard, Death Metal, Berserker''s Shield, The Cosmic Horror,
    Spear of Desolation, Hydra''s Lament, Spear of the Magus, Damaru, Breastplate
    of Valor, The Reaper, Lernaean Bow, Obsidian Shard, Golden Blade, Chronos'' Pendant,
    Tekko-Kagi, Runeforged Hammer, Bragi''s Harp, Freya''s Tears, Bracer of The Abyss,
    Kinetic Cuirass, Blood-Bound Book, Amanita Charm, Shield of the Phoenix, Pharaoh''s
    Curse, Eye of Providence, Bancroft''s Talon, Oni Hunter''s Garb, Helm of Radiance,
    Pendulum Blade, Doom Orb, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.43
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.37
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Amanita Charm
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
    this god: Amanita Charm, Soul Gem, Rod of Tahuti, Gluttonous Grimoire, Nimble
    Ring, Shield of the Phoenix, Berserker''s Shield, The Crusher, Rod of Asclepius,
    The Reaper, Kinetic Cuirass, Genji''s Guard, Jotunn''s Revenge, Blood-Bound Book,
    Chandra''s Grace, Bancroft''s Talon, Death Metal, Breastplate of Valor, Oni Hunter''s
    Garb, Pharaoh''s Curse, Runeforged Hammer, Freya''s Tears, Golden Blade, Damaru,
    Lifebinder, Hydra''s Lament, Phoenix Feather, The Cosmic Horror, Spectral Armor,
    Spear of the Magus, Lernaean Bow, Shogun''s Ofuda, Erosion, Shifter''s Shield,
    Helm of Radiance, Spear of Desolation, Eye of the Storm, Umbral Link, Shield Splitter,
    Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.6
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.25
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Cosmic Horror
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
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
    for this god: Rod of Tahuti, Gluttonous Grimoire, The Crusher, Nimble Ring, Soul
    Gem, Jotunn''s Revenge, The Cosmic Horror, Death Metal, Spear of the Magus, Berserker''s
    Shield, Genji''s Guard, Spear of Desolation, The Reaper, Avenging Blade, Damaru,
    Screeching Gargoyle, Hydra''s Lament, Obsidian Shard, Tekko-Kagi, Lernaean Bow,
    Breastplate of Valor, Golden Blade, Runeforged Hammer, Stone of Binding, Bragi''s
    Harp, Bracer of The Abyss, Kinetic Cuirass, Doom Orb, Chronos'' Pendant, Void
    Shield, Blood-Bound Book, Amanita Charm, The World Stone, Heartseeker, Pharaoh''s
    Curse, Eye of Providence, Freya''s Tears, Toxic Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.47
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.5
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.44
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.39
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
  - Jotunn's Revenge
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
    this god: Rod of Tahuti, Nimble Ring, Gluttonous Grimoire, The Crusher, Soul Gem,
    Jotunn''s Revenge, Berserker''s Shield, Death Metal, Genji''s Guard, Golden Blade,
    The Cosmic Horror, Damaru, Spear of the Magus, Lernaean Bow, Hydra''s Lament,
    Breastplate of Valor, Spear of Desolation, Bracer of The Abyss, The Reaper, Bragi''s
    Harp, Runeforged Hammer, Kinetic Cuirass, Pharaoh''s Curse, Chronos'' Pendant,
    Blood-Bound Book, Amanita Charm, Tekko-Kagi, Obsidian Shard, Eye of Providence,
    Freya''s Tears, Bancroft''s Talon, Oni Hunter''s Garb, Helm of Radiance, Rod of
    Asclepius, Toxic Blade, Shield of the Phoenix, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.3
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.52
    Silverbranch Bow:
      total: 0.62
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.46
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
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
  - The Crusher
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Jotunn''s
    Revenge, Nimble Ring, Genji''s Guard, Gluttonous Grimoire, The Crusher, Breastplate
    of Valor, Hydra''s Lament, Berserker''s Shield, Spear of Desolation, Death Metal,
    Freya''s Tears, Chronos'' Pendant, Shield of the Phoenix, Damaru, The Cosmic Horror,
    Spear of the Magus, Lernaean Bow, Screeching Gargoyle, Chandra''s Grace, Golden
    Blade, Gem of Focus, The Reaper, Kinetic Cuirass, Amanita Charm, Runeforged Hammer,
    Totem of Death, Arondight, Pharaoh''s Curse, Bracer of The Abyss, Pendulum Blade,
    Eye of Providence, Oni Hunter''s Garb, Blood-Bound Book, Tekko-Kagi, Obsidian
    Shard, Bragi''s Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.31
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.31
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.66
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
    Underrated for this god: Rod of Tahuti, Nimble Ring, Gluttonous Grimoire, The
    Crusher, Soul Gem, Jotunn''s Revenge, Death Metal, Berserker''s Shield, Genji''s
    Guard, Damaru, The Cosmic Horror, Hydra''s Lament, Lernaean Bow, Spear of the
    Magus, Spear of Desolation, Golden Blade, The Reaper, Bragi''s Harp, Breastplate
    of Valor, Runeforged Hammer, Bracer of The Abyss, Tekko-Kagi, Chronos'' Pendant,
    Obsidian Shard, Blood-Bound Book, Kinetic Cuirass, Pharaoh''s Curse, Amanita Charm,
    Bancroft''s Talon, Freya''s Tears, Helm of Radiance, Eye of Providence, Oni Hunter''s
    Garb, Rod of Asclepius, Shield of the Phoenix, Deathbringer, Shogun''s Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: hybrid
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Nimble Ring, Gluttonous
    Grimoire, The Crusher, Soul Gem, Jotunn''s Revenge, Death Metal, Berserker''s
    Shield, Genji''s Guard, Damaru, The Cosmic Horror, Hydra''s Lament, Lernaean Bow,
    Spear of the Magus, Spear of Desolation, Golden Blade, The Reaper, Bragi''s Harp,
    Breastplate of Valor, Runeforged Hammer, Bracer of The Abyss, Tekko-Kagi, Chronos''
    Pendant, Obsidian Shard, Blood-Bound Book, Kinetic Cuirass, Pharaoh''s Curse,
    Amanita Charm, Bancroft''s Talon, Freya''s Tears, Helm of Radiance, Eye of Providence,
    Oni Hunter''s Garb, Rod of Asclepius, Shield of the Phoenix, Deathbringer, Shogun''s
    Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Nimble Ring:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.47
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.34
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.29
  swaps:
  - added: Silverbranch Bow
    removed: Death Metal
    reason: community 79% win over 32 matches (vs 58% on this god), taking the model's
      weakest slot from Death Metal
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, The Crusher,
    Jotunn''s Revenge, The Reaper, Death Metal, Amanita Charm, Berserker''s Shield,
    Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Genji''s Guard, Shield
    of the Phoenix, Damaru, The Cosmic Horror, Hydra''s Lament, Runeforged Hammer,
    Spear of the Magus, Chandra''s Grace, Golden Blade, Spear of Desolation, Kinetic
    Cuirass, Breastplate of Valor, Lernaean Bow, Oni Hunter''s Garb, Chronos'' Pendant,
    Lifebinder, Obsidian Shard, Pharaoh''s Curse, Bragi''s Harp, Jade Scepter, Avenging
    Blade, Freya''s Tears, Bracer of The Abyss, Eye of Providence, Spectral Armor,
    Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.57
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.25
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: mana-stack
  slot_order:
  - Bancroft's Talon
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Bancroft's Talon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Soul Gem, Gluttonous Grimoire, Nimble Ring, Jotunn''s Revenge, The
    Crusher, Death Metal, The Reaper, Bancroft''s Talon, Genji''s Guard, Blood-Bound
    Book, Amanita Charm, Rod of Asclepius, Hydra''s Lament, Berserker''s Shield, Shield
    of the Phoenix, Damaru, The Cosmic Horror, Breastplate of Valor, Runeforged Hammer,
    Spear of the Magus, Chandra''s Grace, Spear of Desolation, Golden Blade, Oni Hunter''s
    Garb, Kinetic Cuirass, Lernaean Bow, Chronos'' Pendant, Bragi''s Harp, Lifebinder,
    Obsidian Shard, Jade Scepter, Helm of Radiance, Yogi''s Necklace, Avenging Blade,
    Bracer of The Abyss, Freya''s Tears, Pharaoh''s Curse, Transcendence, Eye of Providence.'
  slot_scores:
    Bancroft's Talon:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.52
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.42
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.2
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.33
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: crit
  slot_order:
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - The Crusher
  - Deathbringer
  flex_slots:
  - Damaru
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Rod of Tahuti, Gluttonous Grimoire, Nimble Ring, The Crusher,
    Jotunn''s Revenge, Berserker''s Shield, The Reaper, Death Metal, Amanita Charm,
    Blood-Bound Book, Rod of Asclepius, Genji''s Guard, Bancroft''s Talon, Shield
    of the Phoenix, Damaru, The Cosmic Horror, Golden Blade, Spear of the Magus, Chandra''s
    Grace, Hydra''s Lament, Runeforged Hammer, Kinetic Cuirass, Breastplate of Valor,
    Spear of Desolation, Lernaean Bow, Pharaoh''s Curse, Oni Hunter''s Garb, Bracer
    of The Abyss, Chronos'' Pendant, Bragi''s Harp, Lifebinder, Obsidian Shard, Jade
    Scepter, Freya''s Tears, Eye of Providence, Tekko-Kagi, Spectral Armor.'
  slot_scores:
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.44
    Riptalon:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.6
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.29
    Damaru:
      total: 0.52
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.31
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.34
    Deathbringer:
      total: 0.47
      efficiency: 0.45
      win: 0.6
      pick: 0.0
      fit: 0.31
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Nimble Ring,
    The Crusher, The Reaper, Amanita Charm, Genji''s Guard, Death Metal, Shield of
    the Phoenix, Berserker''s Shield, Blood-Bound Book, Rod of Asclepius, The Cosmic
    Horror, Bancroft''s Talon, Spear of Desolation, Hydra''s Lament, Spear of the
    Magus, Chandra''s Grace, Damaru, Breastplate of Valor, Runeforged Hammer, Kinetic
    Cuirass, Golden Blade, Chronos'' Pendant, Obsidian Shard, Oni Hunter''s Garb,
    Lernaean Bow, Freya''s Tears, Lifebinder, Pharaoh''s Curse, Tekko-Kagi, Eye of
    Providence, Jade Scepter, Spectral Armor, Bragi''s Harp, Helm of Radiance, Bracer
    of The Abyss.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.12
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.41
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.29
    The Crusher:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.59
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.84
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Rod of Tahuti, Gluttonous Grimoire, Shield
    of the Phoenix, Nimble Ring, The Reaper, Berserker''s Shield, The Crusher, Rod
    of Asclepius, Blood-Bound Book, Kinetic Cuirass, Jotunn''s Revenge, Genji''s Guard,
    Bancroft''s Talon, Chandra''s Grace, Death Metal, Breastplate of Valor, Oni Hunter''s
    Garb, Runeforged Hammer, Freya''s Tears, Damaru, Lifebinder, Hydra''s Lament,
    Phoenix Feather, Pharaoh''s Curse, The Cosmic Horror, Spectral Armor, Golden Blade,
    Spear of the Magus, Umbral Link, Erosion, Shifter''s Shield, Helm of Radiance,
    Spear of Desolation, Eye of the Storm, Shield Splitter, Eye of Providence, Lernaean
    Bow, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.59
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.58
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.2
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.32
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.76
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - The Cosmic Horror
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Cosmic Horror
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Rod of Tahuti, Gluttonous Grimoire, The Crusher, Jotunn''s
    Revenge, Nimble Ring, The Reaper, Amanita Charm, The Cosmic Horror, Death Metal,
    Avenging Blade, Berserker''s Shield, Spear of the Magus, Blood-Bound Book, Genji''s
    Guard, Rod of Asclepius, Shield of the Phoenix, Bancroft''s Talon, Spear of Desolation,
    Damaru, Screeching Gargoyle, Hydra''s Lament, Runeforged Hammer, Obsidian Shard,
    Chandra''s Grace, Kinetic Cuirass, Breastplate of Valor, Void Shield, Golden Blade,
    Tekko-Kagi, Oni Hunter''s Garb, Stone of Binding, Lernaean Bow, Void Stone, Chronos''
    Pendant, Lifebinder, Pharaoh''s Curse, Doom Orb, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.44
    Death Metal:
      total: 0.53
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.41
    The Cosmic Horror:
      total: 0.53
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.6
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.65
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.35
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
  starter: *id001
  aspect: Aspect of Strife
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
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Soul Gem, Nimble Ring, Gluttonous Grimoire, The Crusher,
    Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Golden Blade, The Reaper,
    Death Metal, Genji''s Guard, Rod of Asclepius, Shield of the Phoenix, Blood-Bound
    Book, Bancroft''s Talon, The Cosmic Horror, Damaru, Chandra''s Grace, Spear of
    the Magus, Hydra''s Lament, Lernaean Bow, Runeforged Hammer, Kinetic Cuirass,
    Breastplate of Valor, Pharaoh''s Curse, Spear of Desolation, Oni Hunter''s Garb,
    Bracer of The Abyss, Bragi''s Harp, Chronos'' Pendant, Lifebinder, Obsidian Shard,
    Eye of Providence, Shogun''s Ofuda, Freya''s Tears, Toxic Blade, Tekko-Kagi.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.61
      efficiency: 0.53
      win: 0.67
      pick: 0.3
      fit: 0.69
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.31
  starter: *id001
  aspect: Aspect of Strife
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
  - The Crusher
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Rod of Tahuti, Gluttonous
    Grimoire, Jotunn''s Revenge, Nimble Ring, Genji''s Guard, Shield of the Phoenix,
    The Crusher, Chandra''s Grace, Breastplate of Valor, Amanita Charm, Hydra''s Lament,
    The Reaper, Berserker''s Shield, Spear of Desolation, Blood-Bound Book, Death
    Metal, Rod of Asclepius, Freya''s Tears, Bancroft''s Talon, Chronos'' Pendant,
    Damaru, Kinetic Cuirass, The Cosmic Horror, Runeforged Hammer, Spear of the Magus,
    Oni Hunter''s Garb, Screeching Gargoyle, Golden Blade, Gem of Focus, Pharaoh''s
    Curse, Lernaean Bow, Totem of Death, Arondight, Eye of Providence, Spectral Armor,
    Pendulum Blade, Lifebinder, Obsidian Shard.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.26
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.23
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.6
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Rod of Tahuti, Gluttonous Grimoire, Nimble
    Ring, The Crusher, Jotunn''s Revenge, The Reaper, Death Metal, Amanita Charm,
    Berserker''s Shield, Blood-Bound Book, Rod of Asclepius, Bancroft''s Talon, Genji''s
    Guard, Shield of the Phoenix, Damaru, The Cosmic Horror, Hydra''s Lament, Runeforged
    Hammer, Spear of the Magus, Chandra''s Grace, Golden Blade, Spear of Desolation,
    Kinetic Cuirass, Breastplate of Valor, Lernaean Bow, Oni Hunter''s Garb, Chronos''
    Pendant, Lifebinder, Obsidian Shard, Pharaoh''s Curse, Bragi''s Harp, Jade Scepter,
    Avenging Blade, Freya''s Tears, Bracer of The Abyss, Eye of Providence, Spectral
    Armor, Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of Strife
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Rod of Tahuti, Gluttonous
    Grimoire, Nimble Ring, The Crusher, Jotunn''s Revenge, The Reaper, Death Metal,
    Amanita Charm, Berserker''s Shield, Blood-Bound Book, Rod of Asclepius, Bancroft''s
    Talon, Genji''s Guard, Shield of the Phoenix, Damaru, The Cosmic Horror, Hydra''s
    Lament, Runeforged Hammer, Spear of the Magus, Chandra''s Grace, Golden Blade,
    Spear of Desolation, Kinetic Cuirass, Breastplate of Valor, Lernaean Bow, Oni
    Hunter''s Garb, Chronos'' Pendant, Lifebinder, Obsidian Shard, Pharaoh''s Curse,
    Bragi''s Harp, Jade Scepter, Avenging Blade, Freya''s Tears, Bracer of The Abyss,
    Eye of Providence, Spectral Armor, Helm of Radiance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.58
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.52
      win: 0.79
      pick: 0.26
      fit: 0.25
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.6
      pick: 0.0
      fit: 0.27
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.77
  swaps:
  - added: Silverbranch Bow
    removed: Death Metal
    reason: community 79% win over 32 matches (vs 58% on this god), taking the model's
      weakest slot from Death Metal
  starter: *id001
  aspect: Aspect of Strife
---
