---
type: smite-build
god: Nut
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Cosmos
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.53
  slot_order:
  - name: Tyrfing
    pick_rate: 0.38
    win_rate: 0.44
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.35
      win_rate: 0.54
    - name: Book of Thoth
      pick_rate: 0.05
      win_rate: 0.65
  - name: Bragi's Harp
    pick_rate: 0.26
    win_rate: 0.46
    alternates:
    - name: Staff of Myrddin
      pick_rate: 0.18
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.45
  - name: Barbed Carver
    pick_rate: 0.13
    win_rate: 0.51
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.53
    - name: Soul Gem
      pick_rate: 0.09
      win_rate: 0.51
  - name: Rod of Tahuti
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.46
    - name: The Executioner
      pick_rate: 0.14
      win_rate: 0.52
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.52
    alternates:
    - name: The Executioner
      pick_rate: 0.07
      win_rate: 0.4
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.64
  - name: Riptalon
    pick_rate: 0.05
    win_rate: 0.68
    alternates:
    - name: Evil Eye
      pick_rate: 0.05
      win_rate: 0.5
    - name: Obsidian Shard
      pick_rate: 0.04
      win_rate: 0.73
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.24
    win_rate: 0.47
  - name: Archmage's Gem
    pick_rate: 0.16
    win_rate: 0.57
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/nut/
  last_verified: '2026-08-22'
  god_win_rate: 0.4985632183908046
  god_matches_won: 347
  god_matches_played: 696
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-22'
  god_matches_analyzed: 14126
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Riptalon
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Berserker''s
    Shield, Spear of the Magus, Death Metal, The Crusher, Tekko-Kagi, The Reaper,
    Lernaean Bow, Silverbranch Bow, Bracer of The Abyss, Heartseeker, Genji''s Guard,
    Hydra''s Lament, Golden Blade, Breastplate of Valor, Doom Orb, The Cosmic Horror,
    The World Stone, Helm of Radiance, Runeforged Hammer, Chronos'' Pendant, Dreamer''s
    Idol, Dominance, Titan''s Bane, Blood-Bound Book, Pharaoh''s Curse, Freya''s Tears,
    Ancient Signet, Ethereal Staff, Amanita Charm, Toxic Blade, Rod of Asclepius,
    Kinetic Cuirass.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.19
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.45
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.16
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.48
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.54
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.38
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Death Metal, Berserker''s
    Shield, The Crusher, Hydra''s Lament, Spear of the Magus, Genji''s Guard, Heartseeker,
    Lernaean Bow, Breastplate of Valor, The Reaper, Tekko-Kagi, Doom Orb, Runeforged
    Hammer, Ancient Signet, The World Stone, Dominance, Bracer of The Abyss, Golden
    Blade, Helm of Radiance, Chronos'' Pendant, The Cosmic Horror, Silverbranch Bow,
    Bancroft''s Talon, Titan''s Bane, Ethereal Staff, Freya''s Tears, Wish-Granting
    Pearl, Blood-Bound Book, Rod of Asclepius, Amanita Charm, Dreamer''s Idol, Transcendence.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.52
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.42
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.45
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.4
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Riptalon
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Nimble Ring, The Crusher,
    Spear of the Magus, Berserker''s Shield, The Reaper, Death Metal, Tekko-Kagi,
    Genji''s Guard, Heartseeker, Hydra''s Lament, Breastplate of Valor, Lernaean Bow,
    Silverbranch Bow, Doom Orb, The Cosmic Horror, The World Stone, Titan''s Bane,
    Chronos'' Pendant, Freya''s Tears, Bracer of The Abyss, Golden Blade, Runeforged
    Hammer, Dreamer''s Idol, Helm of Radiance, Pendulum Blade, Amanita Charm, Toxic
    Blade, Dominance, Kinetic Cuirass, Ancient Signet, Ethereal Staff, Pharaoh''s
    Curse, Arondight.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.16
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.16
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.56
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.52
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Rod of Tahuti
  - Amanita Charm
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
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Shield of the Phoenix, Ethereal Staff, Rod of Asclepius, Nimble Ring,
    The Reaper, Kinetic Cuirass, Blood-Bound Book, Freya''s Tears, Genji''s Guard,
    Breastplate of Valor, Pharaoh''s Curse, Bancroft''s Talon, The Crusher, Death
    Metal, Spear of the Magus, Runeforged Hammer, Chandra''s Grace, Shogun''s Ofuda,
    Yogi''s Necklace, Phoenix Feather, Lifebinder, Helm of Radiance, Golden Blade,
    Shield Splitter, Sphere of Negation, Lernaean Bow, Mantle Of Discord, Stone of
    Binding, Spectral Armor, Eye of the Storm, Hydra''s Lament, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.13
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.3
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.66
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.25
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire, Nimble Ring, Spear
    of the Magus, The Crusher, The Reaper, Tekko-Kagi, Berserker''s Shield, Silverbranch
    Bow, Heartseeker, Death Metal, Doom Orb, The Cosmic Horror, The World Stone, Avenging
    Blade, Screeching Gargoyle, Dreamer''s Idol, Stone of Binding, Titan''s Bane,
    Lernaean Bow, Genji''s Guard, Toxic Blade, Breastplate of Valor, Bracer of The
    Abyss, Hydra''s Lament, Golden Blade, Runeforged Hammer, Helm of Radiance, Pendulum
    Blade, Amanita Charm, Chronos'' Pendant, Freya''s Tears, Avatar''s Parashu, Kinetic
    Cuirass, Ancient Signet.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.16
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.55
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.13
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.57
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.62
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
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
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous Grimoire, Berserker''s
    Shield, Silverbranch Bow, Golden Blade, Spear of the Magus, Death Metal, The Crusher,
    Lernaean Bow, Tekko-Kagi, The Reaper, Toxic Blade, Genji''s Guard, Bracer of The
    Abyss, Breastplate of Valor, Hydra''s Lament, Heartseeker, Runeforged Hammer,
    Helm of Radiance, Doom Orb, The Cosmic Horror, Amanita Charm, Pharaoh''s Curse,
    Chronos'' Pendant, Freya''s Tears, The World Stone, Dominance, Kinetic Cuirass,
    Ancient Signet, Ethereal Staff, Dreamer''s Idol, Blood-Bound Book, Rod of Asclepius,
    Titan''s Bane.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.16
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.48
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Berserker''s
    Shield, Hydra''s Lament, Freya''s Tears, Chronos'' Pendant, The Crusher, Spear
    of the Magus, Shield of the Phoenix, Death Metal, Screeching Gargoyle, Lernaean
    Bow, The Reaper, Tekko-Kagi, Arondight, Gem of Focus, Silverbranch Bow, Pendulum
    Blade, Totem of Death, Heartseeker, Bracer of The Abyss, Golden Blade, Amanita
    Charm, Runeforged Hammer, Kinetic Cuirass, Pharaoh''s Curse, Doom Orb, Helm of
    Radiance, The Cosmic Horror, Chandra''s Grace, The World Stone, Dominance.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.65
      pick: 0.05
      fit: 0.1
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.6
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.1
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.6
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.26
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.51
      pick: 0.14
      fit: 0.78
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
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
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Gluttonous
    Grimoire, Berserker''s Shield, Spear of the Magus, Death Metal, The Crusher, Tekko-Kagi,
    The Reaper, Lernaean Bow, Silverbranch Bow, Bracer of The Abyss, Heartseeker,
    Genji''s Guard, Hydra''s Lament, Golden Blade, Breastplate of Valor, Doom Orb,
    The Cosmic Horror, The World Stone, Helm of Radiance, Runeforged Hammer, Chronos''
    Pendant, Dreamer''s Idol, Dominance, Titan''s Bane, Blood-Bound Book, Pharaoh''s
    Curse, Freya''s Tears, Ancient Signet, Ethereal Staff, Amanita Charm, Toxic Blade,
    Rod of Asclepius, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.48
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.38
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Riptalon
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Nimble Ring, Soul
    Gem, Gluttonous Grimoire, Berserker''s Shield, Spear of the Magus, Death Metal,
    The Crusher, Tekko-Kagi, The Reaper, Lernaean Bow, Silverbranch Bow, Bracer of
    The Abyss, Heartseeker, Genji''s Guard, Hydra''s Lament, Golden Blade, Breastplate
    of Valor, Doom Orb, The Cosmic Horror, The World Stone, Helm of Radiance, Runeforged
    Hammer, Chronos'' Pendant, Dreamer''s Idol, Dominance, Titan''s Bane, Blood-Bound
    Book, Pharaoh''s Curse, Freya''s Tears, Ancient Signet, Ethereal Staff, Amanita
    Charm, Toxic Blade, Rod of Asclepius, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.45
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.36
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.54
      pick: 0.35
      fit: 0.48
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.68
      pick: 0.15
      fit: 0.54
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.54
      pick: 0.23
      fit: 0.38
  swaps:
  - added: Riptalon
    removed: Spear of the Magus
    reason: community 68% win over 35 matches (vs 50% on this god), taking the model's
      weakest slot from Spear of the Magus
  starter: *id001
---
