---
type: smite-build
god: Hades
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Daybreak Gavel
    pick_rate: 0.2
    win_rate: 0.65
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.65
    - name: Bancroft's Talon
      pick_rate: 0.14
      win_rate: 0.57
  - name: The World Stone
    pick_rate: 0.22
    win_rate: 0.7
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.62
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.65
  - name: Shifter's Shield
    pick_rate: 0.12
    win_rate: 0.65
    alternates:
    - name: The World Stone
      pick_rate: 0.21
      win_rate: 0.61
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.69
  - name: Rod of Tahuti
    pick_rate: 0.23
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.66
    - name: The World Stone
      pick_rate: 0.06
      win_rate: 0.68
  - name: Evil Eye
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.18
      win_rate: 0.67
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.65
  - name: Obsidian Shard
    pick_rate: 0.06
    win_rate: 0.74
    alternates:
    - name: Evil Eye
      pick_rate: 0.08
      win_rate: 0.61
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.6
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.37
    win_rate: 0.68
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.59
  - name: Pendulum of The Ages
    pick_rate: 0.12
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/hades/
  last_verified: '2026-08-10'
  god_win_rate: 0.617595818815331
  god_matches_won: 709
  god_matches_played: 1148
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, Kinetic Cuirass, Spear
    of the Magus, Amanita Charm, The Cosmic Horror, Breastplate of Valor, Oni Hunter''s
    Garb, Rod of Asclepius, Shield of the Phoenix, Helm of Radiance, Jade Scepter,
    Chronos'' Pendant, Ethereal Staff, Wish-Granting Pearl, Spectral Armor, Doom Orb,
    Erosion, Blood-Bound Book, Alchemist Coat, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.74
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.19
      fit: 0.6
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.65
      pick: 0.0
      fit: 0.47
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.47
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Gluttonous Grimoire
  - Spear of Desolation
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - Spear of the Magus
  - The World Stone
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, Spear of the Magus, Breastplate
    of Valor, The Cosmic Horror, Kinetic Cuirass, Amanita Charm, Shield of the Phoenix,
    Death Metal, Oni Hunter''s Garb, Chronos'' Pendant, Rod of Asclepius, Helm of
    Radiance, Jade Scepter, Spectral Armor, Doom Orb, Dreamer''s Idol, Blood-Bound
    Book, Ethereal Staff, Wish-Granting Pearl, Gem of Focus, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.24
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.62
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.19
      fit: 0.56
    Spear of the Magus:
      total: 0.56
      efficiency: 0.6
      win: 0.65
      pick: 0.0
      fit: 0.4
    The World Stone:
      total: 0.56
      efficiency: 0.49
      win: 0.7
      pick: 0.3
      fit: 0.4
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Gluttonous Grimoire, Shield of the Phoenix,
    Rod of Asclepius, Kinetic Cuirass, Genji''s Guard, Blood-Bound Book, Chandra''s
    Grace, Oni Hunter''s Garb, Breastplate of Valor, Spear of the Magus, Lifebinder,
    The Cosmic Horror, Phoenix Feather, Erosion, Helm of Radiance, Spectral Armor,
    Jade Scepter, Eye of Providence, Draconic Scale, Bancroft''s Talon, Sphere of
    Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.66
      pick: 0.2
      fit: 0.42
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.63
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.81
    Soul Gem:
      total: 0.63
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.89
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  - The World Stone
  - Obsidian Shard
  flex_slots:
  - Spear of Desolation
  - The Cosmic Horror
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Spear of the Magus, The Cosmic Horror,
    Genji''s Guard, Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Breastplate
    of Valor, Doom Orb, Stone of Binding, Void Shield, Dreamer''s Idol, Oni Hunter''s
    Garb, Rod of Asclepius, Shield of the Phoenix, Void Stone, Helm of Radiance, Jade
    Scepter, Chronos'' Pendant, Spectral Armor, Blood-Bound Book.'
  slot_scores:
    Gluttonous Grimoire:
      total: 0.65
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.81
    Spear of Desolation:
      total: 0.59
      efficiency: 0.52
      win: 0.65
      pick: 0.19
      fit: 0.68
    The Cosmic Horror:
      total: 0.58
      efficiency: 0.58
      win: 0.65
      pick: 0.0
      fit: 0.58
    Spear of the Magus:
      total: 0.59
      efficiency: 0.6
      win: 0.65
      pick: 0.0
      fit: 0.58
    The World Stone:
      total: 0.59
      efficiency: 0.49
      win: 0.7
      pick: 0.3
      fit: 0.58
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Obsidian Shard
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, Kinetic Cuirass, Amanita
    Charm, Breastplate of Valor, Spear of the Magus, Bracer of The Abyss, The Cosmic
    Horror, Oni Hunter''s Garb, Death Metal, Blood-Bound Book, Helm of Radiance, Bragi''s
    Harp, Rod of Asclepius, Shield of the Phoenix, Nimble Ring, Jade Scepter, Spectral
    Armor, Chronos'' Pendant, Yogi''s Necklace, Ethereal Staff, Wish-Granting Pearl,
    Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.13
    Bracer of The Abyss:
      total: 0.54
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.52
      efficiency: 0.49
      win: 0.65
      pick: 0.0
      fit: 0.38
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.65
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.5
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Spear of Desolation
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Obsidian Shard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Soul Gem, Gluttonous
    Grimoire, Breastplate of Valor, Shield of the Phoenix, Kinetic Cuirass, Amanita
    Charm, Chronos'' Pendant, Chandra''s Grace, Screeching Gargoyle, Spear of the
    Magus, Oni Hunter''s Garb, The Cosmic Horror, Gem of Focus, Gladiator''s Shield,
    Spectral Armor, Death Metal, Rod of Asclepius, Helm of Radiance, Jade Scepter,
    Prophetic Cloak, Yogi''s Necklace, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.66
      pick: 0.2
      fit: 0.51
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.65
      pick: 0.19
      fit: 0.61
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.26
    Soul Gem:
      total: 0.6
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The
    Crusher, Soul Gem, Berserker''s Shield, Genji''s Guard, Hydra''s Lament, Kinetic
    Cuirass, Death Metal, Amanita Charm, Spear of the Magus, Runeforged Hammer, Breastplate
    of Valor, Golden Blade, The Cosmic Horror, Lernaean Bow, Oni Hunter''s Garb, Pharaoh''s
    Curse, Bragi''s Harp, Eye of the Storm, The Reaper, Rod of Asclepius, Shield of
    the Phoenix, Helm of Radiance, Shield Splitter, Damaru, Bracer of The Abyss, Jade
    Scepter, Riptalon, Avenging Blade, Chronos'' Pendant, Triton''s Conch, Spectral
    Armor, Heartseeker, Tekko-Kagi, Blood-Bound Book, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.16
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Obsidian Shard
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    The Crusher, Soul Gem, Genji''s Guard, Berserker''s Shield, Spear of the Magus,
    Kinetic Cuirass, Amanita Charm, Death Metal, Hydra''s Lament, The Cosmic Horror,
    Breastplate of Valor, Runeforged Hammer, Oni Hunter''s Garb, Rod of Asclepius,
    Helm of Radiance, Jade Scepter, Shield of the Phoenix, Chronos'' Pendant, Eye
    of the Storm, The Reaper, Golden Blade, Shield Splitter, Triton''s Conch, Blood-Bound
    Book, Lernaean Bow, Spectral Armor, Ethereal Staff, Damaru, Wish-Granting Pearl,
    Avenging Blade, Bragi''s Harp, Pharaoh''s Curse, Heartseeker, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.18
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.21
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.48
    Gluttonous Grimoire:
      total: 0.62
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.49
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - The Cosmic Horror
  - Spear of the Magus
  flex_slots:
  - The Cosmic Horror
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Soul Gem, Genji''s Guard, Kinetic
    Cuirass, Spear of the Magus, Amanita Charm, The Cosmic Horror, Breastplate of
    Valor, Oni Hunter''s Garb, Rod of Asclepius, Shield of the Phoenix, Helm of Radiance,
    Jade Scepter, Chronos'' Pendant, Ethereal Staff, Wish-Granting Pearl, Spectral
    Armor, Doom Orb, Erosion, Blood-Bound Book, Bancroft''s Talon, Alchemist Coat.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.74
    Spear of Desolation:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.19
      fit: 0.6
    The Cosmic Horror:
      total: 0.57
      efficiency: 0.58
      win: 0.65
      pick: 0.0
      fit: 0.47
    Spear of the Magus:
      total: 0.57
      efficiency: 0.6
      win: 0.65
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The World Stone
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - The World Stone
  - Rod of Tahuti
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Genji''s
    Guard, Kinetic Cuirass, Spear of the Magus, Amanita Charm, The Cosmic Horror,
    Breastplate of Valor, Oni Hunter''s Garb, Rod of Asclepius, Shield of the Phoenix,
    Helm of Radiance, Jade Scepter, Chronos'' Pendant, Ethereal Staff, Wish-Granting
    Pearl, Spectral Armor, Doom Orb, Erosion, Blood-Bound Book, Bancroft''s Talon,
    Alchemist Coat.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.65
      pick: 0.0
      fit: 0.24
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.63
      efficiency: 0.66
      win: 0.65
      pick: 0.0
      fit: 0.74
    The World Stone:
      total: 0.57
      efficiency: 0.49
      win: 0.7
      pick: 0.3
      fit: 0.47
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.44
      win: 0.7
      pick: 0.38
      fit: 0.47
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.74
      pick: 0.18
      fit: 0.47
  swaps:
  - added: Rod of Tahuti
    removed: Spear of Desolation
    reason: community 70% win over 264 matches (vs 62% on this god), taking the model's
      weakest slot from Spear of Desolation
  - added: The World Stone
    removed: The Cosmic Horror
    reason: community 70% win over 253 matches (vs 62% on this god), taking the model's
      weakest slot from The Cosmic Horror
  - added: Obsidian Shard
    removed: Spear of the Magus
    reason: community 74% win over 69 matches (vs 62% on this god), taking the model's
      weakest slot from Spear of the Magus
  starter: *id001
---
