---
type: smite-build
god: Chronos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relativity
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.47
  slot_order:
  - name: Book of Thoth
    pick_rate: 0.35
    win_rate: 0.49
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.22
      win_rate: 0.42
    - name: Tyrfing
      pick_rate: 0.07
      win_rate: 0.48
  - name: Spear of Desolation
    pick_rate: 0.23
    win_rate: 0.49
    alternates:
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.49
    - name: Nimble Ring
      pick_rate: 0.05
      win_rate: 0.48
  - name: Nimble Ring
    pick_rate: 0.28
    win_rate: 0.55
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.57
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.33
  - name: Rod of Tahuti
    pick_rate: 0.26
    win_rate: 0.41
    alternates:
    - name: Nimble Ring
      pick_rate: 0.12
      win_rate: 0.49
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.42
  - name: Obsidian Shard
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.51
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.41
  - name: Evil Eye
    pick_rate: 0.07
    win_rate: 0.33
    alternates:
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.71
    - name: Rod of Tahuti
      pick_rate: 0.05
      win_rate: 0.58
  community_starters:
  - name: Pendulum of the Ages
    pick_rate: 0.29
    win_rate: 0.54
  - name: Sands Of Time
    pick_rate: 0.23
    win_rate: 0.28
  - name: Conduit Gem
    pick_rate: 0.08
    win_rate: 0.35
  source_url: https://smitebrain.com/gods/chronos/
  last_verified: '2026-08-21'
  god_win_rate: 0.4732334047109208
  god_matches_won: 221
  god_matches_played: 467
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer of The Abyss,
    Genji''s Guard, Death Metal, Breastplate of Valor, Bragi''s Harp, Doom Orb, The
    Cosmic Horror, Helm of Radiance, Chronos'' Pendant, The World Stone, Blood-Bound
    Book, Ancient Signet, Dreamer''s Idol, Ethereal Staff, Freya''s Tears, Amanita
    Charm, Rod of Asclepius, Kinetic Cuirass, Bancroft''s Talon, Gem of Focus, Jade
    Scepter, Wish-Granting Pearl.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.2
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.56
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.46
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.36
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.46
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Gluttonous Grimoire, Death Metal, Spear of the Magus, Genji''s Guard, Breastplate
    of Valor, Bragi''s Harp, Doom Orb, Ancient Signet, The World Stone, Helm of Radiance,
    Bracer of The Abyss, Chronos'' Pendant, The Cosmic Horror, Amanita Charm, Freya''s
    Tears, Ethereal Staff, Bancroft''s Talon, Rod of Asclepius, Kinetic Cuirass, Wish-Granting
    Pearl, Blood-Bound Book, Dreamer''s Idol, Jade Scepter, Gem of Focus.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.25
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.16
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.16
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.42
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.39
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Nimble Ring
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Death Metal
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Death Metal, Genji''s
    Guard, Breastplate of Valor, Bragi''s Harp, Doom Orb, The Cosmic Horror, Freya''s
    Tears, Chronos'' Pendant, The World Stone, Bracer of The Abyss, Dreamer''s Idol,
    Helm of Radiance, Amanita Charm, Kinetic Cuirass, Ancient Signet, Ethereal Staff,
    Shield of the Phoenix, Rod of Asclepius, Blood-Bound Book, Gem of Focus, Eye of
    Providence, Screeching Gargoyle.'
  slot_scores:
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.39
    Death Metal:
      total: 0.47
      efficiency: 0.61
      win: 0.48
      pick: 0.0
      fit: 0.28
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.49
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.35
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.35
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Ethereal Staff, Rod of Asclepius, Kinetic Cuirass, Blood-Bound Book, Freya''s
    Tears, Genji''s Guard, Breastplate of Valor, Bancroft''s Talon, Chandra''s Grace,
    Spear of the Magus, Yogi''s Necklace, Phoenix Feather, Lifebinder, Shifter''s
    Shield, Helm of Radiance, Sphere of Negation, Mantle Of Discord, Stone of Binding,
    Spectral Armor, Death Metal, Erosion.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.44
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.37
    Spear of Desolation:
      total: 0.48
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.3
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.24
    Obsidian Shard:
      total: 0.47
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.34
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Doom Orb, The
    Cosmic Horror, The World Stone, Screeching Gargoyle, Stone of Binding, Dreamer''s
    Idol, Genji''s Guard, Breastplate of Valor, Death Metal, Bracer of The Abyss,
    Helm of Radiance, Amanita Charm, Chronos'' Pendant, Freya''s Tears, Bragi''s Harp,
    Kinetic Cuirass, Ancient Signet, Void Shield, Ethereal Staff, Blood-Bound Book,
    Rod of Asclepius, Void Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.16
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.45
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.56
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.48
    Obsidian Shard:
      total: 0.51
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Gluttonous Grimoire, Death Metal, Spear of the Magus, Bragi''s
    Harp, Bracer of The Abyss, Genji''s Guard, Breastplate of Valor, Helm of Radiance,
    Doom Orb, Amanita Charm, Chronos'' Pendant, The Cosmic Horror, Freya''s Tears,
    Kinetic Cuirass, Ancient Signet, The World Stone, Ethereal Staff, Blood-Bound
    Book, Rod of Asclepius, Dreamer''s Idol, Bancroft''s Talon, Eye of Providence,
    Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.41
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.49
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.48
      pick: 0.0
      fit: 0.64
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.38
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.3
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, Freya''s Tears, Chronos'' Pendant, Shield of the
    Phoenix, Spear of the Magus, Death Metal, Screeching Gargoyle, Gem of Focus, Amanita
    Charm, Bragi''s Harp, Totem of Death, Kinetic Cuirass, Bracer of The Abyss, Helm
    of Radiance, Chandra''s Grace, Doom Orb, The Cosmic Horror, Eye of Providence,
    Ancient Signet, Ethereal Staff, The World Stone, Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.09
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.3
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.3
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.51
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.21
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.68
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Spear of Desolation
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Gluttonous Grimoire,
    The Crusher, Death Metal, The Reaper, Tyrfing, Spear of the Magus, Golden Blade,
    Heartseeker, Hydra''s Lament, Riptalon, Berserker''s Shield, Runeforged Hammer,
    Tekko-Kagi, Lernaean Bow, Bragi''s Harp, Silverbranch Bow, Titan''s Bane, Genji''s
    Guard, Breastplate of Valor, Doom Orb, The Cosmic Horror, Helm of Radiance, The
    World Stone, Chronos'' Pendant, Shield Splitter, Amanita Charm, Freya''s Tears,
    Dreamer''s Idol, Ancient Signet, Kinetic Cuirass, Arondight, Avenging Blade, Blood-Bound
    Book, Ethereal Staff, Toxic Blade, Dominance.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.17
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.5
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.35
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.42
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Spear of Desolation
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Gluttonous
    Grimoire, Death Metal, Berserker''s Shield, Tyrfing, The Crusher, Riptalon, Spear
    of the Magus, Golden Blade, Silverbranch Bow, Bragi''s Harp, The Reaper, Lernaean
    Bow, Tekko-Kagi, Hydra''s Lament, Heartseeker, Genji''s Guard, Runeforged Hammer,
    Breastplate of Valor, Bracer of The Abyss, Helm of Radiance, Doom Orb, The Cosmic
    Horror, Toxic Blade, The World Stone, Chronos'' Pendant, Titan''s Bane, Amanita
    Charm, Ancient Signet, Dominance, Ethereal Staff, Dreamer''s Idol, Blood-Bound
    Book, Freya''s Tears, Kinetic Cuirass, Rod of Asclepius, Pharaoh''s Curse.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.18
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.43
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.18
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.45
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.41
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Bracer of The Abyss
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bracer
    of The Abyss, Genji''s Guard, Death Metal, Breastplate of Valor, Bragi''s Harp,
    Doom Orb, The Cosmic Horror, Helm of Radiance, Chronos'' Pendant, The World Stone,
    Blood-Bound Book, Ancient Signet, Dreamer''s Idol, Ethereal Staff, Freya''s Tears,
    Amanita Charm, Rod of Asclepius, Kinetic Cuirass, Bancroft''s Talon, Gem of Focus,
    Jade Scepter, Wish-Granting Pearl.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.56
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.46
    Spear of the Magus:
      total: 0.48
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.36
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Nimble Ring
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s
    Guard, Spectral Armor, Breastplate of Valor, Spear of the Magus, Kinetic Cuirass,
    Doublet of Binding, Freya''s Tears, Erosion, Void Stone, Void Shield, Stampede,
    Bracer of The Abyss, Lifebinder, Shield of the Phoenix, Death Metal, Chronos''
    Pendant, Ethereal Staff, Triton''s Conch, Screeching Gargoyle, Helm of Radiance,
    Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.11
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.42
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.39
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.25
    Obsidian Shard:
      total: 0.47
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.35
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Death Metal, Genji''s
    Guard, Triton''s Conch, Spectral Armor, Spear of the Magus, Breastplate of Valor,
    Bragi''s Harp, Kinetic Cuirass, Doublet of Binding, Erosion, Lifebinder, Ancient
    Signet, Doom Orb, Freya''s Tears, Void Stone, Helm of Radiance, Ethereal Staff,
    Void Shield, The World Stone, Stampede, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.23
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.19
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.14
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.36
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.33
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.82
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Spear of
    the Magus, Genji''s Guard, Spectral Armor, Death Metal, Breastplate of Valor,
    Triton''s Conch, Freya''s Tears, Kinetic Cuirass, Doublet of Binding, Erosion,
    Void Stone, Bragi''s Harp, Doom Orb, Lifebinder, Void Shield, The Cosmic Horror,
    Stampede, Chronos'' Pendant, The World Stone, Helm of Radiance, Ethereal Staff.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.13
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.35
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.44
    Spear of the Magus:
      total: 0.47
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.31
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.31
    Obsidian Shard:
      total: 0.48
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.41
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Rod of Tahuti
  - Spectral Armor
  - Amanita Charm
  - Erosion
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Rod of Asclepius, Shield of the Phoenix, Gluttonous
    Grimoire, Lifebinder, Spectral Armor, Kinetic Cuirass, Ethereal Staff, Erosion,
    Umbral Link, Freya''s Tears, Genji''s Guard, Doublet of Binding, Breastplate of
    Valor, Void Shield, Stampede, Void Stone, Blood-Bound Book, Chandra''s Grace,
    Yogi''s Necklace, Phoenix Feather, Bancroft''s Talon, Shifter''s Shield, Spear
    of the Magus, Mantle Of Discord.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.6
      win: 0.48
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.19
    Spectral Armor:
      total: 0.5
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.95
    Erosion:
      total: 0.49
      efficiency: 0.51
      win: 0.48
      pick: 0.0
      fit: 0.65
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 1.0
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: anti-tank
  slot_order:
  - Nimble Ring
  - Void Shield
  - Void Stone
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Obsidian Shard
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Gluttonous Grimoire, Amanita Charm, Void Stone, Void Shield,
    Spear of the Magus, Rod of Asclepius, Screeching Gargoyle, Stone of Binding, Genji''s
    Guard, Spectral Armor, Breastplate of Valor, Kinetic Cuirass, Doublet of Binding,
    Erosion, Doom Orb, The Cosmic Horror, Freya''s Tears, The World Stone, Dreamer''s
    Idol, Stampede, Lifebinder, Death Metal, Shield of the Phoenix, Bracer of The
    Abyss.'
  slot_scores:
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.35
    Void Shield:
      total: 0.49
      efficiency: 0.47
      win: 0.48
      pick: 0.0
      fit: 0.76
    Void Stone:
      total: 0.5
      efficiency: 0.45
      win: 0.48
      pick: 0.0
      fit: 0.82
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.49
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.38
    Obsidian Shard:
      total: 0.49
      efficiency: 0.54
      win: 0.48
      pick: 0.32
      fit: 0.48
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Rod of Asclepius, Genji''s
    Guard, Spectral Armor, Breastplate of Valor, Death Metal, Kinetic Cuirass, Doublet
    of Binding, Erosion, Spear of the Magus, Freya''s Tears, Triton''s Conch, Void
    Stone, Bragi''s Harp, Void Shield, Stampede, Bracer of The Abyss, Lifebinder,
    Shield of the Phoenix, Chronos'' Pendant, Ethereal Staff, Helm of Radiance, Screeching
    Gargoyle.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.48
      pick: 0.0
      fit: 0.31
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.55
      pick: 0.44
      fit: 0.38
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.48
      pick: 0.0
      fit: 0.53
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.32
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.21
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.8
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Amanita Charm, Genji''s
    Guard, Gluttonous Grimoire, Breastplate of Valor, Rod of Asclepius, Freya''s Tears,
    Spectral Armor, Shield of the Phoenix, Chronos'' Pendant, Kinetic Cuirass, Doublet
    of Binding, Screeching Gargoyle, Erosion, Spear of the Magus, Death Metal, Void
    Stone, Void Shield, Stampede, Triton''s Conch, Gem of Focus, Lifebinder, Bragi''s
    Harp, Totem of Death, Bracer of The Abyss.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.49
      pick: 0.35
      fit: 0.08
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.27
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.45
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.19
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.92
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Pharaoh's Curse
  - Soul Gem
  flex_slots:
  - The Crusher
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Amanita Charm,
    Gluttonous Grimoire, The Crusher, Pharaoh''s Curse, Rod of Asclepius, Shogun''s
    Ofuda, Death Metal, Berserker''s Shield, The Reaper, Golden Blade, Hydra''s Lament,
    Genji''s Guard, Runeforged Hammer, Triton''s Conch, Spectral Armor, Tyrfing, Sanguine
    Lash, Heartseeker, Spear of the Magus, Breastplate of Valor, Riptalon, Kinetic
    Cuirass, Doublet of Binding, Lernaean Bow, Erosion, Freya''s Tears, Tekko-Kagi,
    Silverbranch Bow, Void Stone, Titan''s Bane, Shield Splitter, Void Shield, Stampede,
    Eye of the Storm, Bragi''s Harp, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.36
    The Crusher:
      total: 0.49
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.24
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.0
      fit: 0.51
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.83
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Pharaoh's Curse
  - Shogun's Ofuda
  - Soul Gem
  flex_slots:
  - Pharaoh's Curse
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Jotunn''s Revenge, Amanita
    Charm, Gluttonous Grimoire, Pharaoh''s Curse, Rod of Asclepius, Shogun''s Ofuda,
    Berserker''s Shield, Death Metal, The Crusher, Golden Blade, Spear of the Magus,
    Tyrfing, Triton''s Conch, Spectral Armor, Genji''s Guard, Riptalon, Silverbranch
    Bow, Lernaean Bow, The Reaper, Hydra''s Lament, Breastplate of Valor, Runeforged
    Hammer, Bragi''s Harp, Kinetic Cuirass, Doublet of Binding, Sanguine Lash, Erosion,
    Tekko-Kagi, Freya''s Tears, Lifebinder, Heartseeker, Void Stone, Void Shield,
    Helm of Radiance, Toxic Blade, Stampede, Ethereal Staff.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.48
      pick: 0.0
      fit: 0.39
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.39
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.29
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.55
      win: 0.48
      pick: 0.0
      fit: 0.57
    Shogun's Ofuda:
      total: 0.49
      efficiency: 0.53
      win: 0.48
      pick: 0.0
      fit: 0.57
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.85
  starter: *id001
  aspect: Aspect of Relativity
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Rod of Tahuti
  - Spectral Armor
  - Soul Gem
  flex_slots:
  - Spectral Armor
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Soul Gem, Amanita Charm, Gluttonous Grimoire, Rod of
    Asclepius, Genji''s Guard, Spectral Armor, Breastplate of Valor, Spear of the
    Magus, Kinetic Cuirass, Doublet of Binding, Freya''s Tears, Erosion, Void Stone,
    Void Shield, Stampede, Bracer of The Abyss, Lifebinder, Shield of the Phoenix,
    Death Metal, Chronos'' Pendant, Ethereal Staff, Triton''s Conch, Screeching Gargoyle,
    Helm of Radiance, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.48
      pick: 0.0
      fit: 0.21
    Breastplate of Valor:
      total: 0.47
      efficiency: 0.65
      win: 0.48
      pick: 0.0
      fit: 0.14
    Spear of Desolation:
      total: 0.49
      efficiency: 0.57
      win: 0.49
      pick: 0.31
      fit: 0.39
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.86
      win: 0.41
      pick: 0.43
      fit: 0.25
    Spectral Armor:
      total: 0.47
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.48
      pick: 0.0
      fit: 0.87
  starter: *id001
  aspect: Aspect of Relativity
---
