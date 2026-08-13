---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.08
  aspect_win_rate: 1.0
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.42
    win_rate: 0.6
    alternates:
    - name: Transcendence
      pick_rate: 0.31
      win_rate: 0.54
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.6
  - name: Transcendence
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.63
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.57
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.67
  - name: The Reaper
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.58
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.67
  - name: The Crusher
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.57
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Skeggox
      pick_rate: 0.1
      win_rate: 0.5
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.33
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.29
    win_rate: 0.51
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.74
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-13'
  god_win_rate: 0.5555555555555556
  god_matches_won: 70
  god_matches_played: 126
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Lernaean Bow
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
    this god: Gluttonous Grimoire, The Reaper, Death Metal, Lernaean Bow, Berserker''s
    Shield, Damaru, Soul Gem, Riptalon, Golden Blade, Tekko-Kagi, Silverbranch Bow,
    Genji''s Guard, Bragi''s Harp, Spear of the Magus, Dominance, Tyrfing, The Cosmic
    Horror, Bracer of The Abyss, Runeforged Hammer, Breastplate of Valor, Pharaoh''s
    Curse, Demon Blade, Obsidian Shard, Spear of Desolation, Deathbringer, Kinetic
    Cuirass, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb, Avenging Blade, Nimble
    Ring, Pendulum Blade, Shield Splitter, Eye of Providence, Eros'' Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
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
    god: Gluttonous Grimoire, Soul Gem, The Reaper, Genji''s Guard, Spear of the Magus,
    Death Metal, Spear of Desolation, The Cosmic Horror, Berserker''s Shield, Riptalon,
    Breastplate of Valor, Lernaean Bow, Obsidian Shard, Silverbranch Bow, Damaru,
    Bracer of The Abyss, Chronos'' Pendant, Tekko-Kagi, Bragi''s Harp, Golden Blade,
    Runeforged Hammer, The World Stone, Doom Orb, Freya''s Tears, Dreamer''s Idol,
    Blood-Bound Book, Pendulum Blade, Bancroft''s Talon, Helm of Radiance, Gem of
    Focus, Dominance, Pharaoh''s Curse, Kinetic Cuirass, Tyrfing, Shield of the Phoenix,
    Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.56
    Death Metal:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.5
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
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
    this god: Amanita Charm, The Reaper, Berserker''s Shield, Soul Gem, Gluttonous
    Grimoire, Shield of the Phoenix, Riptalon, Kinetic Cuirass, Rod of Asclepius,
    Genji''s Guard, Pharaoh''s Curse, Oni Hunter''s Garb, Golden Blade, Blood-Bound
    Book, Chandra''s Grace, Bancroft''s Talon, Breastplate of Valor, Runeforged Hammer,
    Lernaean Bow, Death Metal, Shogun''s Ofuda, Phoenix Feather, Freya''s Tears, Spectral
    Armor, Damaru, Shifter''s Shield, Erosion, Eye of the Storm, Shield Splitter,
    Eye of Providence, Lifebinder, Spear of the Magus, Draconic Scale, Leviathan''s
    Hide, Silverbranch Bow, Yogi''s Necklace, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.3
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.49
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.57
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Spear of the Magus
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Spear of the Magus
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
    for this god: Gluttonous Grimoire, The Reaper, Soul Gem, Riptalon, Silverbranch
    Bow, Spear of the Magus, Tekko-Kagi, The Cosmic Horror, Berserker''s Shield, Death
    Metal, Lernaean Bow, Obsidian Shard, Avenging Blade, Spear of Desolation, Damaru,
    Genji''s Guard, Golden Blade, Screeching Gargoyle, Breastplate of Valor, The World
    Stone, Doom Orb, Runeforged Hammer, Pendulum Blade, Dreamer''s Idol, Toxic Blade,
    Dominance, Bracer of The Abyss, Bragi''s Harp, Tyrfing, Pharaoh''s Curse, Stone
    of Binding, Kinetic Cuirass, Void Shield, Amanita Charm, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.57
    Spear of the Magus:
      total: 0.55
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.43
    The Crusher:
      total: 0.6
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.67
    Titan's Bane:
      total: 0.55
      efficiency: 0.45
      win: 0.63
      pick: 0.4
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
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
    this god: Riptalon, Gluttonous Grimoire, Berserker''s Shield, Silverbranch Bow,
    Golden Blade, The Reaper, Soul Gem, Lernaean Bow, Tyrfing, Genji''s Guard, Death
    Metal, Damaru, Bracer of The Abyss, Pharaoh''s Curse, Spear of the Magus, Tekko-Kagi,
    Breastplate of Valor, Dominance, Bragi''s Harp, Toxic Blade, The Cosmic Horror,
    Nimble Ring, Runeforged Hammer, Blood-Bound Book, Kinetic Cuirass, Shogun''s Ofuda,
    Bancroft''s Talon, Amanita Charm, Oni Hunter''s Garb, Obsidian Shard, Eros'' Bow,
    Eye of Providence, Spear of Desolation, Freya''s Tears, Demon Blade, Qin''s Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Soul Gem
  flex_slots:
  - The Crusher
  - Hydra's Lament
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, Spear of Desolation, Berserker''s Shield, Chronos''
    Pendant, Freya''s Tears, The Reaper, Death Metal, Shield of the Phoenix, Spear
    of the Magus, Lernaean Bow, Gem of Focus, Riptalon, The Cosmic Horror, Damaru,
    Screeching Gargoyle, Bracer of The Abyss, Silverbranch Bow, Chandra''s Grace,
    Arondight, Pendulum Blade, Golden Blade, Obsidian Shard, Pharaoh''s Curse, Bragi''s
    Harp, Kinetic Cuirass, Runeforged Hammer, Amanita Charm, Blood-Bound Book, Oni
    Hunter''s Garb, Tekko-Kagi, Bancroft''s Talon, Helm of Radiance, Dominance, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.59
    Hydra's Lament:
      total: 0.55
      efficiency: 0.58
      win: 0.56
      pick: 0.19
      fit: 0.55
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.34
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
  - Genji's Guard
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Death Metal,
    Spear of the Magus, The Reaper, Genji''s Guard, The Cosmic Horror, Spear of Desolation,
    Berserker''s Shield, Bracer of The Abyss, Bragi''s Harp, Lernaean Bow, Chronos''
    Pendant, Obsidian Shard, Breastplate of Valor, Damaru, Riptalon, Blood-Bound Book,
    Bancroft''s Talon, Helm of Radiance, Silverbranch Bow, Golden Blade, Rod of Asclepius,
    Gem of Focus, The World Stone, Doom Orb, Nimble Ring, Jade Scepter, Runeforged
    Hammer, Dreamer''s Idol, Tekko-Kagi, Ancient Signet, Freya''s Tears, Dominance,
    Pharaoh''s Curse, Tyrfing, Kinetic Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.46
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Spear of the Magus
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Death Metal,
    Soul Gem, The Reaper, Spear of the Magus, Berserker''s Shield, The Cosmic Horror,
    Lernaean Bow, Bragi''s Harp, Damaru, Bracer of The Abyss, Genji''s Guard, Riptalon,
    Obsidian Shard, Golden Blade, Spear of Desolation, Silverbranch Bow, Tekko-Kagi,
    Runeforged Hammer, Dominance, Blood-Bound Book, Tyrfing, Breastplate of Valor,
    Bancroft''s Talon, Helm of Radiance, Chronos'' Pendant, The World Stone, Doom
    Orb, Nimble Ring, Rod of Asclepius, Dreamer''s Idol, Pharaoh''s Curse, Jade Scepter,
    Kinetic Cuirass, Triton''s Conch, Ancient Signet.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.44
    Death Metal:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.51
    Spear of the Magus:
      total: 0.54
      efficiency: 0.6
      win: 0.6
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Lernaean Bow
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
    Underrated for this god: Gluttonous Grimoire, Death Metal, Lernaean Bow, Berserker''s
    Shield, Damaru, Soul Gem, Riptalon, Golden Blade, Tekko-Kagi, Silverbranch Bow,
    Genji''s Guard, Bragi''s Harp, Spear of the Magus, Dominance, Tyrfing, The Reaper,
    The Cosmic Horror, Bracer of The Abyss, Runeforged Hammer, Breastplate of Valor,
    Pharaoh''s Curse, Demon Blade, Obsidian Shard, Spear of Desolation, Deathbringer,
    Kinetic Cuirass, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb, Avenging
    Blade, Nimble Ring, Pendulum Blade, Shield Splitter, Eye of Providence, Eros''
    Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.6
      pick: 0.42
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.22
      fit: 0.54
  starter: *id001
---
